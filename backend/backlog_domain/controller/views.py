from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from backlog_domain.service.backlog_domain_service_impl import BacklogDomainServiceImpl


class BacklogDomainView(viewsets.ViewSet):
    backlogDomainService = BacklogDomainServiceImpl.getInstance()

    def createBacklogDomain(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        domain = data.get('domain')

        createdBacklogDomain = self.backlogDomainService.createBacklogDomain(backlogId, domain).domain

        return Response(createdBacklogDomain, status=status.HTTP_200_OK)

    def modifyBacklogDomain(self, request):
        data = request.data
        backlogId = data.get('backlogId')
        domain = data.get('domain')

        modifiedBacklogDomain = self.backlogDomainService.modifyBacklogDomain(backlogId, domain).domain

        return Response(modifiedBacklogDomain, status=status.HTTP_200_OK)